"""
Coupon Code Validator
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:
code[i]: a string representing the coupon identifier.
businessLine[i]: a string denoting the business category of the coupon.
isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:
code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.
"""
import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_coupons = []
        for i in range(len(code)):
            if (
                bool(re.match(r'^[A-Za-z0-9_]+$', code[i])) and
                businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"] and
                isActive[i]
            ):
                valid_coupons.append((businessLine[i], code[i]))
        priority = { "electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3 }
        valid_coupons = sorted(valid_coupons, key=lambda x: (priority.get(x[0]), x[1]))
        return [x[1] for x in valid_coupons]