# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    map = Hash.new
    for i in 0..strs.length - 1
        sorted = strs[i].chars.sort.join
        if map.key?(sorted)
            map[sorted] = [strs[i], *map[sorted]]
        else
            map[sorted] = [strs[i]]
        end
    end
    map.values
end