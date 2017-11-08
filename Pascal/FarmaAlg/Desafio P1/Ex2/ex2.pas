program ex2;

var
n, num1, num2, a: real;

begin
	readln(n);
	num1 := (n * 100)/ 60;
	num2 := (n * 100)/ 70;
	if num1 >= 87.00 then
		writeln('O preço original para 30% é: ', num1:0:2)
	else
		writeln('O preço original para 40% é: ', num2:0:2);
	readln(a);
end.