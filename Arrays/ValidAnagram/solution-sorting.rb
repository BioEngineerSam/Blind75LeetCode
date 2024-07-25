# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    hash_set = Set.new
    # if the lengths are not equal, this is not an anagram
    return false if s.length != t.length
    # if string broken up into characters and sorted are equal they must be anagrams
    return s.chars.sort == t.chars.sort
end