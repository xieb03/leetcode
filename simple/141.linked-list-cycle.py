# 141. 环形链表
# 给你一个链表的头节点 head ，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/linked-list-cycle/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return F"{self.val}"


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        # 注意 set 里面存的是整个 ListNode 而不是 val
        val_set = {head}
        while head.next is not None:
            head = head.next
            if head in val_set:
                return True
            val_set.add(head)
        return False


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 注意 set 里面存的是整个 ListNode 而不是 val
        val_set = set()
        while head:
            if head in val_set:
                return True
            val_set.add(head)
            head = head.next
        return False


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # 快慢指针，假设进入环之后（环的大小是 n, 二者都是顺时针走），slow 在第 1 个点，fast 在第 k 个点 (n >= k > 1)，那么从顺时针的方向，
    # fast 落后 n - (k - 1) 个距离, 而每走一次，fast 都会往前追一个距离，所以 n - (k - 1) 步以后，二者重合，
    # 这个时候 slow 并没有跑完一圈，因此说时间复杂度是 O(n)，即 slow 最多遍历整个数组一次，而不会第二次进入到环
    # 注意为什么要求 slow = 1，这样 slow 不会跳跃，能保证在一个周期内完成，否则可以假设 slow 非常大，尽管也能相遇，其实总用时一致，因为要在环内运动多次
    # 注意为什么要求 fast = slow + 1，这样能保证每次二者的距离减小1，所以最终一定能相遇，而如果是其他值，那么二者的间距会是一个同余的值，并不保证能相遇
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        # 因为 fast 走的快，所以不用再针对 slow 进行判断了
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def make_linked_list(head: List, pos: int) -> Optional[ListNode]:
    if len(head) == 0:
        return None
    root_list_node = ListNode(head[0])
    current_parent_node = root_list_node
    # 构造单链
    for value in head[1:]:
        new_list_node = ListNode(value)
        current_parent_node.next = new_list_node
        current_parent_node = new_list_node
    # 增加环
    if pos >= 0:
        # 按顺序遍历链表，直到找到第 pos 个
        index = 0
        first_list_node = root_list_node
        while index != pos:
            first_list_node = first_list_node.next
            index += 1
        # 将尾部的 next 指向第 pos 个，完成环的添加
        current_parent_node.next = first_list_node
    return root_list_node


def main():
    # == 默认比较内存地址
    assert not ListNode(1) == ListNode(1)
    x = ListNode(1)
    assert x == x

    for clazz in (Solution, Solution_1, Solution_2):
        solution = clazz()
        assert solution.hasCycle(make_linked_list(head=[3, 2, 0, -4], pos=1))
        assert solution.hasCycle(make_linked_list(head=[1, 2], pos=0))
        assert not solution.hasCycle(make_linked_list(head=[11], pos=-1))
        assert not solution.hasCycle(make_linked_list(head=[], pos=-1))


if __name__ == '__main__':
    main()
