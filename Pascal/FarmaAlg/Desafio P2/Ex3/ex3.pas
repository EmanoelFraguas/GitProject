program exp3;

var

cont, i, result2, zeros, num2, soma: longint;
v1: array[1..100] of integer;
mediaTot: real;
num, n, mult, result1: longint;

procedure contador(n: longint);

begin
	num := n;
	cont := 0;
	while num > 0 do
	begin
		num := num div 10;
		cont := cont +1;
	end;
end;

procedure insertArray(n: longint);

begin
	mult := 1;
	zeros := 0;
	for i := cont downto 1 do
	begin
		result1 := n mod (mult * 10);
		result2 := result1 div mult;
		mult := mult * 10;
		v1[i] := result2;
		//if result2 = 0 then
			//zeros := zeros + 1;
	end;
end;

procedure printArray();

begin
	write('Array: ');
	for i := 1 to cont do
		write(v1[i], ' ');
	writeln('');
end;

procedure media();

begin
	soma := 0;
	for i := 1 to cont do
	begin
		soma := soma + v1[i];	
	end;
	mediaTot := soma /(cont - zeros);
	writeln(mediaTot:0:2);
end;

begin
    read(n);
	num2 := n;
    contador(n);
	insertArray(n);
	//printArray();   
	media();
end.