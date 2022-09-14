
class MashFactory:
    def __init__(self, answer_bank):
        self.answer_bank = answer_bank

    # Reset pointer when category doesnt have enough items to iterate through
    def skip_category(self, point_cat, total_cats):
        return (point_cat+1)%total_cats

    # How much to reset pointer by at end of list
    def pointer_reset(self, x, y):
        mod = x%y
        if mod<0:
            mod+=y
        return mod
    
    def get_fortune(self):
        # Instantiate list of categories
        all_categories = list(self.answer_bank.keys())
        # Instantiate pointer to move through keys and values 
        pointer = {"category_pointer": 0, "index_pointer": 0}
        user_number = int(input("Now for the biggest decision of your life... Choose a number between 1 and 10: "))
        counter = user_number * 10 - 1
        fortune = {}
        done = False
        while not done:
            category_pointer = pointer["category_pointer"]
            index_pointer = pointer["index_pointer"] 
            current_list = self.answer_bank[all_categories[category_pointer]]
            remaining_items = len(current_list) - index_pointer
            if counter < remaining_items:
                pointer["index_pointer"] += counter
                self.answer_bank[all_categories[category_pointer]].pop(pointer['index_pointer'])
                
                if len(self.answer_bank[all_categories[category_pointer]]) == 1:
                    fortune[all_categories[category_pointer]] = self.answer_bank[all_categories[category_pointer]][0]
                    del self.answer_bank[all_categories[category_pointer]] 
                    all_categories.pop(category_pointer)
                    if len(all_categories)!=0:
                        pointer['index_pointer'] = 0
                        pointer['category_pointer'] = self.pointer_reset(category_pointer, len(all_categories))
                
                counter = user_number - 1
            
            else:
                counter -= remaining_items
                pointer['category_pointer'] = self.skip_category(category_pointer, len(all_categories))
                pointer['index_pointer'] = 0
            done = len(self.answer_bank.keys()) == 0
        return fortune
