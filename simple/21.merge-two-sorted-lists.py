# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/merge-two-sorted-lists/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def make_linked_list(head: List) -> Optional[ListNode]:
    # 可以传入空数组，返回 None
    if len(head) == 0:
        return None
    root_list_node = ListNode(head[0])
    current_parent_node = root_list_node
    # 构造单链
    for value in head[1:]:
        new_list_node = ListNode(value)
        current_parent_node.next = new_list_node
        current_parent_node = new_list_node
    return root_list_node


def get_list_node_val_list(a: ListNode):
    if a:
        val_list = [a.val]
        while a.next is not None:
            a = a.next
            val_list.append(a.val)
        return val_list
    return []


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    # 递归
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        # 先找到第一个
        if list1.val > list2.val:
            result = list2
            list2 = list2.next
        else:
            result = list1
            list1 = list1.next
        # 递归找到下一个
        result.next = self.mergeTwoLists(list1, list2)
        return result


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_2:
    # 将递归变为循环
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        # 先找到第一个
        if list1.val < list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next
        # 要保留对头结点的引用，因为后面会不断后移
        root = result
        # 比较 list1 和 list2，判断哪一个要进行扩展
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        # 退出循环后，至少有一个为 None，把不是 None 的直接加在后面即可
        if list1:
            result.next = list1
        else:
            result.next = list2
        return root


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # Solution_2 的改进版，避免"找到第一个"的重复代码
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        # 构造一个虚拟头结点，最后只要返回虚拟头结点的 next 即可，避免"找到第一个"的重复代码
        # 要保留对头结点的引用，因为后面会不断后移
        root = ListNode(-1)
        current_root = root
        # 比较 list1 和 list2，判断哪一个要进行扩展
        while list1 and list2:
            if list1.val < list2.val:
                current_root.next = list1
                list1 = list1.next
            else:
                current_root.next = list2
                list2 = list2.next
            current_root = current_root.next
        # 退出循环后，至少有一个为 None，把不是 None 的直接加在后面即可
        if list1:
            current_root.next = list1
        else:
            current_root.next = list2

        return root.next


def main():
    for clazz in (Solution, Solution_1, Solution_2):
        solution = clazz()
        assert get_list_node_val_list(
            solution.mergeTwoLists(make_linked_list(head=[]), make_linked_list(head=[]))) == []
        assert get_list_node_val_list(
            solution.mergeTwoLists(make_linked_list(head=[]), make_linked_list(head=[0]))) == [0]
        assert get_list_node_val_list(
            solution.mergeTwoLists(make_linked_list(head=[0]), make_linked_list(head=[]))) == [0]
        assert (get_list_node_val_list(
            solution.mergeTwoLists(make_linked_list(head=[1, 2, 4]), make_linked_list(head=[1, 3, 4])))
                == [1, 1, 2, 3, 4, 4])


if __name__ == '__main__':
    main()
