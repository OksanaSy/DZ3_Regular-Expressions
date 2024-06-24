#3. Find the occurrence and position of substrings within a string

import re                                                                      
                                                                               
def find_substrings(text, substring):                                          
    pattern = re.compile(substring)                                            
    matches = pattern.finditer(text)                                           
    result = [(match.start(), match.end()) for match in matches]               
    return result                                                              
                                                                               
text = "This is a test text for testing."                                      
substring = "test"                                                             
print(find_substrings(text, substring))                                        
                                                                               
