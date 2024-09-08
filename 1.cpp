// #include <iostream>
// #include <string>

// namespace filo{
// struct char_filo_node
// {
//   char_filo_node* next_node;
//   char value;
// };

// class char_filo
// {
//   char_filo_node *first = nullptr;


//   char_filo_node* pop()
//   {
//     if (first == nullptr)
//     {
//         std::cout << "Char filo is empty" << std::endl;
//         return nullptr;
//     }
//     char_filo_node *tmp = first;
//     first = first->next_node;
//     return tmp;
//   }

//   void add(char value)
//   {
//     char_filo_node *tmp = new char_filo_node;
//     tmp->value = value;
//     tmp->next_node = first;
//     first = tmp;
//   }

//   char getValue()
//   {
//     if (first == nullptr)
//     {
//         std::cout << "Char filo is empty" << std::endl;
//         return "";
//     }
//     return first->value;
//   }
// };
// }

// int main(){
//     std::string input;
//     std::cout << "Please, enter the string: \t"; 
//     std::cin >> input;
//     bool string_exists = true;
//     filo::char_filo filo;
//     for (int i = 0; i < input.length(); i++)
//     {
//         switch (input[i])
//         {
//         case '(':
//             /* code */
//             break;
//         case ')':
//             if 
//             break;
//         case ']':
//             /* code */
//             break;
//         case '}':
//             /* code */
//             break;
//         case '(':
//             /* code */
//             break;
        
//         default:
//             break;
//         }
//         if ((input[i] == '(') || (input[i] == '[') || (input[i] == '{'))
//             filo.add(input[i]);
//         else if ((input[i] == ')') || (input[i] == ']') || (input[i] == ']'))
//         {
//             /* code */
//         }
//         if (!string_exists)
//         {
//             std::cout << "String does not exist!" << std::endl;
//             break;
//         }
//     }
//     filo::char_filo_node *tmp = filo.pop();
//     while(tmp != nullptr)
// }