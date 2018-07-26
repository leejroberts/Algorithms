

class Node
  attr_accessor :value, :next_node
  def initialize(value=nil, next_node=nil)
    @value = value
    @next_node = next_node
  end
end

def LinkedList
  attr_accessor :head, :node_count
  def initialize(starting_value)
    @head = Node.new(starting_value)
    @node_count = 1
  end


  def search(value, current_node=self.head)
    if !current_node || (current_node && !current_node.value)
      false
    elsif current_node.value == value
      true
    else
      self.search(value, current_node.next_node)
    end
  end

  def push(value)
    if !self.head.value # if head is valueless, thus the only node
      self.head.value = value
    else
      previous_tail_node = self.return_node(self.node_count-1)
      new_tail_node = Node.new(value)
      previous_tail_node.next_node = new_tail_node
      self.node_count += 1
    end
  end

  def return_node(index)
    if index >= self.node_count || index < 0
      nil
    else
      current_node = self.head
      counter = 0
      while counter < index do
        current_node = current_node.next_node
        counter += 1
      end
      current_node
    end
  end

  def update(value, index)
    update_node = self.return_node(index)
    if update_node
      update_node.value = value
      true
    else
      nil
    end
  end

  def insert(value, index)
    if index == 0 && !self.head.value # if there is only one node and the value is empty
      self.head.value = value
      self.node_count += 1
      true
    elsif index >= node_count || index < 0 # out of index range
      false
    else
      node_before_index = self.return_node(index-1)
      node_at_index = node_before.next_node
      if node_before_index && node_at_index
        insert_node = Node.new(value, next_node=current_node)
        node_before_index.next_node = insert_node
        insert_node.next_node = node_at_index
        self.node_count += 1
        true
      else
        false
      end
  end

  def delete(index)
    if index == 0
      current_head = self.head
      new_head = current_head.next_node
      if new_head
        self.head = new_head
        current_head = nil
        node_count -= 1
        true
      else
        self.head.value = nil
        true
      end
    elsif index < 0 || index >= self.node_count
      false
    else
      node_before_index = self.return_node(index-1)
      node_at_index = node_before_index.next_node
      node_before_index.next_node = node_an_index.next_node
      node_at_index = nil
      self.node_count -= 1
      true
    end
  end

end
