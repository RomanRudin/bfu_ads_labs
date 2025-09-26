public class chek_error// тут мы проверям ощибки на дурока тоже ловим
{
    public bool Opertors(string nombers)
    {
        for (int i = 0; i < nombers.Length-1; i++)
        {
            if ((nombers[i] == '*' || nombers[i] == '-' || nombers[i] == '+' || nombers[i] == '=' || nombers[i] == '/')&&
                (nombers[i + 1] == '*' || nombers[i + 1] == '-' || nombers[i + 1] == '+' || nombers[i + 1] == '/' ||
                 nombers[i + 1] == '='|| i ==0))
                return false;
            if (nombers[i] == '/' && nombers[i + 1] == '0')
                return false;
        }

        if (nombers[nombers.Length-1]!='=')
        {
            return false;
        }
        return true;
    }
    
    public bool Skobki(string s)
    { 
        List<char> satk = new List<char>();

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i]==')')
            {
                if (satk.Count > 0 && satk[satk.Count - 1] == '(')
                    satk.RemoveAt(satk.Count - 1);
                else
                    return false;
            }
            else if (s[i]=='}')
            {
                if (satk.Count > 0 && satk[satk.Count - 1] == '{')
                    satk.RemoveAt(satk.Count - 1);
                else
                    return false;
            }
            else if (s[i]==']')
            {
                if (satk.Count > 0 && satk[satk.Count - 1] == '[')
                    satk.RemoveAt(satk.Count - 1);
                else
                    return false;
            }
            else if(s[i]=='('|| s[i]=='{'||s[i]=='[') 
                satk.Add(s[i]);
        }
        

        if (satk.Count>0)
        {
            return false;
        }

        return true;
    }
}

public class calcul // название можно забить думал 2 класс делать стало лень тут сразу и буду считать 
{
      int Priority(char sim)
      {
            if (sim == '*' || sim == '/')
                  return 3;

            else if (sim == '+' || sim == '-')
                  return 2;
            return 1;
      }

      bool Nomber(char s)
      {
            return (s <= '9' && s >= '0');
      }

      public string First_work(string str) //тут мыделаем хитрую сортировку
      {
            var steck = new Stack<char>();
            string help = "";
            for (int i = 0; i < str.Length; i++)
            {
                  if (Nomber(str[i]))
                  {
                        while (i < str.Length && Nomber(str[i]))
                        {
                              help += str[i];
                              i++;
                        }

                        help += " ";
                        i--;
                  }
                  else if (str[i] == '(') steck.Push(str[i]);
                  else if (str[i] == ')')
                  {
                        while ((steck.Count > 0) && steck.Peek() != '(')
                        {
                              help += steck.Pop();
                              help += ' ';

                        }

                        if (steck.Count > 0)
                              steck.Pop();
                  }
                  else
                  {
                        while ((steck.Count > 0) && Priority(steck.Peek()) >= Priority(str[i]))
                        {
                              help += steck.Pop();
                              help += ' ';

                        }

                        steck.Push(str[i]);
                  }
            }

            while (steck.Count > 0)
            {
                  help += steck.Pop();
                  help += ' ';

            }

            return help;
      }

      public float operation(float a, float b, char sim)
      {
            switch (sim)
            {
                  case '+':
                        return a + b;
                  case '-':
                        return a - b;
                  case '*':
                        return a * b;
                  case '/':
                        return a / b;
                  default:
                        return b;
            }
      }

      public string calculate(string str) // и за счет стека получаем результат
      {
            var steck = new Stack<float>(); //флоат потому что могут быть дробные числа
            int count = 0;
            for (int i = 0; i < str.Length; i++)
            {

                  if (Nomber(str[i]))
                  {
                        string temp = "";
                        while (i < str.Length && Nomber(str[i]))
                        {
                              temp += str[i];
                              i++;
                        }

                        count++;
                        steck.Push(Convert.ToInt32(temp));

                        i--;
                  }

                  else if (steck.Count > 1 && str[i] != ' ')
                  {
                        float b = float.Parse(Convert.ToString(steck.Pop()));

                        float a = float.Parse(Convert.ToString(steck.Pop()));

                        if (b == 0 && str[i] == '/') return "АЯЯЯ на ноль делит незя";

                        steck.Push(operation(a, b, str[i]));




                  }
            }

            return Convert.ToString(steck.Peek());
      }
}

internal class Program
{
    public static void Main(string[] args)
    {
          var test = new calcul();
          var chek = new chek_error();
          Console.WriteLine("Ведите выражение");
          string a = Console.ReadLine();
          if (chek.Opertors(a)&& chek.Skobki(a))
                Console.WriteLine(test.calculate(test.First_work(a)));
          else
                Console.WriteLine("Идиот");

          Console.ReadLine();
    }
}