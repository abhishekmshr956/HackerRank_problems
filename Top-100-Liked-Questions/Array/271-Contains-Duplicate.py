def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # #### solution using set method
        # n = len(nums)
        # set_nums = set(nums)
        # n_set = len(set_nums)
        # return False if n == n_set else True

        # ### solution using hash table
        # freq_map = {}
        # for n in nums:
        #     if n in freq_map:
        #         return True 
        #     freq_map[n] = freq_map.get(n, 0) + 1
        # return False

        # using set
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False

        # a = []
        # for n in nums:
        #     if n in a:
        #         return True
        #     else:
        #         a.append(n)
        # return False