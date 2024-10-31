using System.Drawing;

void setColor(ConsoleColor color) {
    Console.ForegroundColor = color;
}

double getCoeff(ref double x, char coeffName) {
    string? input;
    while (true) {
        Console.Write($"Введите коэффициент {coeffName}: ");
        input = Console.ReadLine();
        if (double.TryParse(input, out double numericValue)) {
            x = numericValue;
            break;
        } else {
            setColor(ConsoleColor.Red);
            Console.WriteLine("Введён неверный коэффициент!");
            Console.ResetColor();
        }
    }
    return x;
}

void solveEquation(in double a, in double b, in double c) {
    setColor(ConsoleColor.Green);
    if (a == 0) {
        if (b == 0) {
            if (c == 0) {
                Console.WriteLine("R");
                return;
            }
            setColor(ConsoleColor.Red);
            Console.WriteLine("Действительных корней нет.");
            return;
        }
        Console.WriteLine(-c / b);
        return;
    }
    double d = b * b - 4 * a * c;
    List<double> roots = [];
    double newRoot;
    if (d == 0) {
        newRoot = -b / (2 * a);
        if (newRoot > 0) {
            roots.Add(Math.Sqrt(newRoot));
            roots.Add(-Math.Sqrt(newRoot));
        } else if (newRoot == 0) {
            roots.Add(0);
        }
    } else if (d > 0) {
        for (int i = 0; i < 2; i++) {
            newRoot = (-b + Math.Pow(-1, i) * Math.Sqrt(d)) / (2 * a);
            if (newRoot > 0) {
                roots.Add(Math.Sqrt(newRoot));
                roots.Add(-Math.Sqrt(newRoot));
            } else if (newRoot == 0) {
                roots.Add(0);
            }
        }
    } else {
        setColor(ConsoleColor.Red);
        Console.WriteLine("Действительных корней нет.");
        return;
    }
    if (roots.Count > 0) {
        Console.WriteLine($"Количество корней: {roots.Count}");
        Console.WriteLine("Корни:");
        foreach (double root in roots) {
            Console.WriteLine($"{root}");
        }
    } else {
        setColor(ConsoleColor.Red);
        Console.WriteLine("Дейтвительных корней нет.");
    }
}

double a = 0, b = 0, c = 0;

getCoeff(ref a, 'a');

getCoeff(ref b, 'b');

getCoeff(ref c, 'c');

solveEquation(a, b, c);