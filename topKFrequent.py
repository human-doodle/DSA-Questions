'''

692. Top K Frequent Words

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

solve it in O(n log(k)) time and O(n) extra space

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 
SOME OBSERVATION:
heapq heappush by default implements min-heap. So inorder to implement maxheap, The easiest way is to invert the value of the keys and use heapq. For example, turn 1000.0 into -1000.0 and 5.0 into -5.0.

'''

import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        
        heap = []
        
        for word, count in freq.items():
                heapq.heappush(heap, (-count, word))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
  
