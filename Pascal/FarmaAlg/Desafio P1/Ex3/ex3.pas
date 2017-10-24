program ex3;

var
a, b, c, n: integer;

begin
	readln(n);
	a := n div 10;
	b := n mod 10;
	while c < n do
	begin
		c := a + b;
		a := b;
		b := c;
	end;
	if (c = n) and (n > 9) then
		writeln('Sim, é um número de Keith.')
	else 
		writeln('Não é um número de Keith.');
end.