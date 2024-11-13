def run_wwc_program(program):
    memory = program.copy()
    
    ip = 0
    
    while ip < len(memory):
        opcode = memory[ip]
        
        if opcode == 99:
            break
            
        pos1, pos2, pos3 = memory[ip + 1], memory[ip + 2], memory[ip + 3]
        
        if opcode == 1:
            memory[pos3] = memory[pos1] + memory[pos2]
        elif opcode == 2:
            memory[pos3] = memory[pos1] * memory[pos2]
        else:
            raise ValueError(f"Unknown operation code: {opcode}")
        
        ip += 4
        
    return memory

program_str = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,2,155,1,9,155,0,99,2,0,14,0"
program = [int(x) for x in program_str.split(',')]

target_output = 19690720
found = False

print("Starting search...")
for noun in range(100):
    for verb in range(100):
        test_program = program.copy()
        
        test_program[1] = noun
        test_program[2] = verb
        
        result = run_wwc_program(test_program)
        
        if result[0] == target_output:
            answer = 100 * noun + verb
            print(f"Found it! Noun: {noun}, Verb: {verb}")
            print(f"Answer (100 * noun + verb) = {answer}")
            found = True
            break
    if found:
        break

if not found:
    print("No solution found")
