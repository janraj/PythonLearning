'''
 First recurring charcter in a string.
 Example,
	ABCA => A
        ABC  => NULL

 An O(n) Solution with bit manipulations. 
'''

def first_recurring_char(strs):
    bit_map = 0
    for i in range(0, len(strs)):
        ch = strs[i].upper()
        ch_pos = (1 << (ord(ch) % 65))
        if bit_map & ch_pos:
            print("Repeating Character is ", ch.upper())     
            return 
        bit_map = bit_map | ch_pos
    print("Repeating Character is None") 
    return    

first_recurring_char("ABCA")
first_recurring_char("ABC")
first_recurring_char("BCABA")
    

    
