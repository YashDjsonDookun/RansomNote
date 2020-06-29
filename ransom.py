#!/usr/bin/python3

class Solution(object):
  def canSpell(self, magazine, note):
    # Fill this in.
    self.magazine = magazine
    self.note = note
    for character in self.note:
        if (character not in self.magazine):
            return False
    return True
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False
