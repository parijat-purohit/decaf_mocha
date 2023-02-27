class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell = prices[0], 0

        for price in prices[1:]:
            buy = min(price, buy)
            sell = max(sell, price-buy)
        return sell

"""
The code is using sliding window approach to solve the problem of finding maximum profit
that can be made from buying and selling a stock at different prices on different days.

The sliding window here consists of a single variable 'buy' that represents
the minimum price seen so far. The 'sell' variable is used to keep track of the maximum profit
seen so far by calculating the difference between the current price and the minimum price
seen so far (i.e., the 'buy' variable).

The window slides forward by iterating through the 'prices' list, updating the 'buy' and 'sell' variables
at each step. Therefore, this approach can be categorized as a sliding window approach.

Time Complexity:
The time complexity of this solution is O(n), where n is the length of the input list 'prices'.
This is because we iterate through the list once, performing a constant number of operations at each step.

Space Complexity:
The space complexity of this solution is O(1), which is constant. This is because we only use two variables,
'buy' and 'sell', to keep track of the minimum price seen so far and the maximum profit seen so far, respectively.
Therefore, the space required does not depend on the length of the input list 'prices'.
"""