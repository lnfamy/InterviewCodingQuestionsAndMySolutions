/*
https://leetcode.com/problems/lru-cache/
*/

class LRUCache {
    //approach: hashmap and double linked list
    private DLinkedNode head;
    private DLinkedNode tail;
    private int capacity;
    private int size;
    private Map<Integer, DLinkedNode> cache = new HashMap<>();

    //internal class: Doubly linked node
    class DLinkedNode {
        int key;
        int value;
        DLinkedNode prev;
        DLinkedNode next;
    }

    private void addNode(DLinkedNode node) {
        node.prev = head;
        node.next = head.next;

        head.next.prev = node;
        head.next = node;
    }

    private void removeNode(DLinkedNode node) {
        DLinkedNode prev = node.prev;
        DLinkedNode next = node.next;

        prev.next = next;
        next.prev = prev;
    }

    private void moveToHead(DLinkedNode node) {
        removeNode(node);
        addNode(node);
    }

    private DLinkedNode popTail() {
        DLinkedNode t = this.tail.prev;
        removeNode(this.tail.prev);
        return t;
    }

    public LRUCache(int capacity) {
        this.size = 0;
        this.capacity = capacity;

        this.head = new DLinkedNode();
        this.tail = new DLinkedNode();
        head.next = tail;
        tail.prev = head;

    }

    public int get(int key) {
        DLinkedNode node = cache.get(key);
        if (node == null) {
            return -1;
        }
        moveToHead(node);
        return node.value;
    }

    public void put(int key, int value) {
        DLinkedNode node = cache.get(key);

        if (node == null) {
            DLinkedNode newNode = new DLinkedNode();
            newNode.key = key;
            newNode.value = value;

            cache.put(key, newNode);
            addNode(newNode);

            this.size++;
            if (this.size > this.capacity) {
                DLinkedNode tail = popTail();
                cache.remove(tail.key);
                this.size--;
            }
        }
        //if it exists, update the value and move to head
        else {
            node.value = value;
            moveToHead(node);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */