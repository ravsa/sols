#include <iostream>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <stack>
namespace singly{
    struct node {
        int data;
        node* next;
    };
    class link 
    {
        node* create_node(int value){
            node* temp = (node*)malloc(sizeof(node));
            temp->data = value;
            temp->next = NULL;
            return temp;
        }
        public:
        node *root;
        node *last;
        link() { 
            root = NULL;
            last = NULL;
        }
        ~link(){
            node *temp = root;
            while(root){
                root = root->next;
                free(temp);
                temp = root;
            }
        }
        void display(){
            node *temp = root;
            while(temp){
                std::cout<<"["<<temp->data<<"]->";
                temp = temp->next;
            }
            std::cout << "NULL"<<std::endl;
        };
        int length(){
            int count = 0;
            node *temp = root;
            while((temp)){
                count++;
                temp = temp->next;
            } 
            return count;
        }
        void insert_rear(int value);
        void insert_front(int value);
        void insert_pos(int loc, int value);
        int delete_front();
        int delete_rear();
        int delete_pos(int loc);
        bool palindrom_recursive(node* tail);
        bool palindrom_stack();
        void reverse();
        void reverse_ij(node*);
        void reverse_stack();
        void sorting_bubble();
        void sorting_selection();
        int find_element(int element);
        void concate(node* s){
            node *temp = root;
            while(temp->next)
                temp = temp->next;
            temp->next = s;
        };
    };

    void link::insert_rear(int value){
        node *temp = create_node(value);
        if(!root){
            root = temp;
            last = temp;
        }
        else{
            last->next = temp;
            last = temp;
        }
    }

    void link::insert_front(int value){
        node *temp = create_node(value);
        if(!root){
            root = temp;
            last = temp;
        }
        else{
            temp->next = root;
            root = temp;
        }
    }

    void link::insert_pos(int loc, int value){
        if(!root){insert_rear(value); return;}
        node *p = root;
        for(int i = 1; i < loc - 1; ++i){
            p = p->next;
        }
        if(!p){
            std::cout << "out of locations" << std::endl;
        }
        else{
            node *temp = create_node(value);
            node *t = p->next;
            p->next = temp;
            temp->next = t;
        }
    }

    int link::delete_rear(){
        if(!root) return INT_MAX;
        node *temp = root;
        int value;
        if(!temp->next){
            value = temp->data;
            root = NULL;
            free(temp);
        }
        else{
            while(temp->next->next){
                temp = temp->next;
            }
            value = temp->next->data;
            free(temp->next);
            temp->next = NULL;
        }
        return value;
    }

    int link::delete_front(){
        if(!root) return INT_MAX;
        node *temp = root;
        int value = root->data;
        root = root->next;
        free(temp);
        return value;
    }

    int link::delete_pos(int loc){
        if(!root || loc == 0) return INT_MAX;
        node *temp = root;
        int value;
        if(loc == 1) {
            value = root->data;
            root = root->next;
            free(temp);
        }
        else{
            for (int i = 1; i < loc - 1; ++i){
                temp = temp->next;
                if(!temp->next) return INT_MAX;
            }
            node *t = temp->next;
            value = temp->next->data;
            temp->next = (temp->next)->next;
            free(t);
        }
        return value;
    }

    bool link::palindrom_recursive(node *tail){
        static node *head = root;
        if(tail){
            if(!palindrom_recursive(tail->next)) return false;
            if(tail->data != head->data) return false;
            head = head->next;
        }
        return true;
    }

    void link::reverse(){
        node *prev = NULL, *current = root, *next;
        while(current){
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        root = prev;
    }

    void link::reverse_ij(node *tail){
        static int i = 1, j = length();
        static node* head = root;
        if(tail){
            reverse_ij(tail->next);
            if(i<=j){
                std::swap(tail->data, head->data);
                head = head->next;
                i++;
                j--;
            }
            else
                return;
        }
    }
    void link::reverse_stack(){
        node *temp = root;
        std::stack<int> s;
        while(temp){
            s.push(temp->data);
            temp = temp->next;
        }
        temp = root;
        while(temp){
            temp->data = s.top();
            s.pop();
            temp = temp->next;
        }
    }

    bool link::palindrom_stack(){
        node *temp = root;
        std::stack<int> s;
        while(temp){
            s.push(temp->data);
            temp = temp->next;
        }
        temp = root;
        while(temp){
            if(temp->data != s.top())
                return false;
            s.pop();
            temp = temp->next;
        }
        return true;
    }

    void link::sorting_bubble(){
        for(node *i = root; i; i = i->next){
            for(node *j = root; j->next; j = j->next){
                if(j->data > j->next->data){
                    std::swap(j->data, j->next->data);
                }
            }
        }
    }

    void link::sorting_selection(){
        node *min;
        for(node *i = root; i; i=i->next){
            min = i;
            for(node *j=i; j; j=j->next){
                if (min->data > j->data)
                    min = j;
            }
            std::swap(i->data, min->data);
        }
    }

    int link::find_element(int element){
        node *temp = root;
        int count = 0;
        while(temp){
            count++;
            if (temp->data == element)
                return count;
            temp = temp->next;
        }
        return INT_MAX;
    }
}
namespace doubly{
    struct node {
        int data;
        node *prev;
        node *next;
    };
    class link
    {
        node *create_node(int value){
            node *temp = (node*)malloc(sizeof(node));
            temp->data = value;
            temp->next = temp->prev = NULL;
            return temp;
        }
        public:
        node *root;
        node *last;
        link() { 
            root = NULL;
            last = NULL;
        }
        ~link(){
            node *temp = root;
            while(root){
                root = root->next;
                free(temp);
                temp = root;
            }
        }
        void display(node *temp){
            while(temp){
                std::cout<<"["<<temp->data<<"]->";
                temp = temp->next;
            }
            std::cout << "NULL"<<std::endl;
        };
        void display_reverse(node *temp){
            while(temp){
                std::cout<<"["<<temp->data<<"]->";
                temp = temp->prev;
            }
            std::cout << "NULL"<<std::endl;
        };
        int length(){
            int count = 0;
            node *temp = root;
            while((temp)){
                count++;
                temp = temp->next;
            } 
            return count;
        }
        void insert_rear(int value);
        void insert_front(int value);
        void insert_pos(int loc, int value);
        int delete_front();
        int delete_rear();
        int delete_pos(int loc);
        bool palindrom_recursive(node *head, node* tail);
        void sorting_bubble();
        void sorting_selection();
        int find_element(int element);
        void concate(node* s){
            node *temp = root;
            while(temp->next)
                temp = temp->next;
            temp->next = s;
        };
    };

    void link::insert_rear(int value){
        node *temp = create_node(value);
        if(!root){
            root = temp;
            last = temp;
        }
        else{
            temp->prev = last;
            last->next = temp;
            last = temp;
        }
    }

    void link::insert_front(int value){
        node *temp = create_node(value);
        if(!root){
            root = temp;
            last = temp;
        }
        else{
            root->prev = temp;
            temp->next = root;
            root = temp;
        }
    }

    void link::insert_pos(int loc, int value){
        if(!root){insert_rear(value); return;}
        node *p = root;
        for(int i = 1; i < loc - 1; ++i){
            p = p->next;
        }
        if(!p){
            std::cout << "out of locations" << std::endl;
        }
        else{
            node *temp = create_node(value);
            node *t = p->next;
            t->prev = temp;
            temp->prev = p;
            p->next = temp;
            temp->next = t;
        }
    }

    int link::delete_rear(){
        if(!root) return INT_MAX;
        node *temp = root;
        int value;
        if(!temp->next){
            value = temp->data;
            root = NULL;
            free(temp);
        }
        else{
            while(temp->next->next){
                temp = temp->next;
            }
            value = temp->next->data;
            free(temp->next);
            temp->next = NULL;
            last = temp;
        }
        return value;
    }

    int link::delete_front(){
        if(!root) return INT_MAX;
        node *temp = root;
        int value = root->data;
        root = root->next;
        root->prev = NULL;
        free(temp);
        return value;
    }

    int link::delete_pos(int loc){
        if(!root || loc == 0) return INT_MAX;
        node *temp = root;
        int value;
        if(loc == 1) {
            value = root->data;
            root = root->next;
            root->prev = NULL;
            free(temp);
        }
        else{
            for (int i = 1; i < loc - 1; ++i){
                temp = temp->next;
                if(!temp->next) return INT_MAX;
            }
            node *t = temp->next;
            value = temp->next->data;
            if ((temp->next->next)){
                temp->next->next->prev = temp;
                temp->next = (temp->next)->next;
            }
            else{
                temp->next = NULL;
                last = temp;
            }
            free(t);
        }
        return value;
    }

    bool link::palindrom_recursive(node *head, node *tail){
        if(head->next != tail && tail->prev != head && head != tail){
            if(!palindrom_recursive(head->next, tail->prev)) return false;
            if(head->data != tail->data) return false;
        }
        return true;
    }

    void link::sorting_bubble(){
        for(node *i = last; i->prev; i = i->prev){
            for(node *j = root; j != i; j = j->next){
                if(j->data > j->next->data){
                    std::swap(j->data, j->next->data);
                }
            }
        }
    }

    void link::sorting_selection(){
        node *min;
        for(node *i = root; i; i=i->next){
            min = i;
            for(node *j=i; j; j=j->next){
                if (min->data > j->data)
                    min = j;
            }
            std::swap(i->data, min->data);
        }
    }
    
    int link::find_element(int element){
        node *temp = root;
        int count = 0;
        while(temp){
            count++;
            if (temp->data == element)
                return count;
            temp = temp->next;
        }
        return INT_MAX;
    }
}

namespace csingly{
    struct node {
        int data;
        node* next;
    };
    class link 
    {
        node* create_node(int value){
            node* temp = (node*)malloc(sizeof(node));
            temp->data = value;
            temp->next = NULL;
            return temp;
        }
        public:
        node *root;
        node *last;
        link() { 
            root = NULL;
            last = NULL;
        }
        ~link(){
            node *temp = root;
            node *end = root;
            while(root && root->next != end ){
                root = root->next;
                free(temp);
                temp = root;
            }
            free(temp);
        }
        void display(){
            node *temp = root;
            while(true && root){
                std::cout<<"["<<temp->data<<"]->";
                if(temp->next == root)
                    break;
                temp = temp->next;
            }
            std::cout << "NULL"<<std::endl;
        };
        int length(){
            int count = 0;
            node *temp = root;
            node *end = root;
            while((temp->next != end)){
                count++;
                temp = temp->next;
            } 
            return count;
        }
        void insert_rear(int value);
        void insert_front(int value);
        void insert_pos(int loc, int value);
        int delete_front();
        int delete_rear();
        int delete_pos(int loc);
        bool palindrom_recursive(node* tail);
        bool palindrom_stack();
        void reverse();
        void reverse_ij(node*);
        void reverse_stack();
        void sorting_bubble();
        void sorting_selection();
        int find_element(int element);
        void concate(node* s){
            node *temp = root;
            while(temp->next)
                temp = temp->next;
            temp->next = s;
        };
    };

    void link::insert_rear(int value){
        node *temp = create_node(value);
        if(!root){
            root = temp;
            root->next = root;
            last = temp;
        }
        else{
            last->next = temp;
            temp->next = root;
            last = temp;
        }
    }

    void link::insert_front(int value){
        node *temp = create_node(value);
        if(!root){
            root = temp;
            root->next = root;
            last = temp;
        }
        else{
            temp->next = root;
            root = temp;
            last->next = root;
        }
    }

    void link::insert_pos(int loc, int value){
        if(!root && loc == 1){insert_rear(value); return;}
        node *p = root;
        for(int i = 1; i < loc - 1; ++i){
            p = p->next;
        }
        if(!p && loc == 0){
            std::cout << "out of locations" << std::endl;
            return ;
        }
        else{
            node *temp = create_node(value);
            node *t = p->next;
            p->next = temp;
            temp->next = t;
        }
    }

    int link::delete_rear(){
        if(!root) return INT_MAX;
        node *temp = root;
        int value;
        if(temp->next == root){
            value = temp->data;
            root = NULL;
            free(temp);
        }
        else{
            while(temp->next->next != root){
                temp = temp->next;
            }
            value = temp->next->data;
            free(temp->next);
            temp->next = root;
        }
        return value;
    }

    int link::delete_front(){
        if(!root) return INT_MAX;
        node *temp = root;
        int value;
        value = root->data;
        if (temp->next == root){
            root = NULL;
            last = NULL;
        }
        else{
            root = root->next;
            last->next = root;
        }
        free(temp);
        return value;
    }

    int link::delete_pos(int loc){
        if(!root || loc == 0) return INT_MAX;
        node *temp = root;
        int value;
        if(loc == 1) {
            value = root->data;
            if (root->next == root)
                root = NULL;
            else
                root = root->next;
            last = root;
            free(temp);
        }
        else{
            for (int i = 1; i < loc - 1; ++i){
                temp = temp->next;
                if(!temp->next) return INT_MAX;
            }
            node *t = temp->next;
            value = temp->next->data;
            temp->next = (temp->next)->next;
            free(t);
        }
        return value;
    }

    bool link::palindrom_recursive(node *tail){
        static node *head = root;
        if(tail){
            if(!palindrom_recursive(tail->next)) return false;
            if(tail->data != head->data) return false;
            head = head->next;
        }
        return true;
    }

    void link::reverse(){
        node *prev = NULL, *current = root, *next;
        while(current){
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        root = prev;
    }

    void link::reverse_ij(node *tail){
        static int i = 1, j = length();
        static node* head = root;
        if(tail){
            reverse_ij(tail->next);
            if(i<=j){
                std::swap(tail->data, head->data);
                head = head->next;
                i++;
                j--;
            }
            else
                return;
        }
    }
    void link::reverse_stack(){
        node *temp = root;
        std::stack<int> s;
        while(temp){
            s.push(temp->data);
            temp = temp->next;
        }
        temp = root;
        while(temp){
            temp->data = s.top();
            s.pop();
            temp = temp->next;
        }
    }

    bool link::palindrom_stack(){
        node *temp = root;
        std::stack<int> s;
        while(temp){
            s.push(temp->data);
            temp = temp->next;
        }
        temp = root;
        while(temp){
            if(temp->data != s.top())
                return false;
            s.pop();
            temp = temp->next;
        }
        return true;
    }

    void link::sorting_bubble(){
        for(node *i = root; i; i = i->next){
            for(node *j = root; j->next; j = j->next){
                if(j->data > j->next->data){
                    std::swap(j->data, j->next->data);
                }
            }
        }
    }

    void link::sorting_selection(){
        node *min;
        for(node *i = root; i; i=i->next){
            min = i;
            for(node *j=i; j; j=j->next){
                if (min->data > j->data)
                    min = j;
            }
            std::swap(i->data, min->data);
        }
    }

    int link::find_element(int element){
        node *temp = root;
        int count = 0;
        while(temp){
            count++;
            if (temp->data == element)
                return count;
            temp = temp->next;
        }
        return INT_MAX;
    }
}

int main()
{
    csingly::link ll;
    ll.insert_rear(1);
    ll.insert_rear(2);
    ll.insert_rear(3);
    ll.insert_rear(4);
    ll.display();
    return 0;
}
