program ex1;

var
v, w: array[1..100] of integer;
cont, i, k, n, soma, lim: integer;

procedure insertV();
begin
	readln(n);
	cont := 1;
	while n <> 0 do
	begin
		v[cont] := n;
		cont:= cont + 1;
		readln(n);
	end;
	cont := cont - 1;
end;

procedure insertW();
begin
	soma := 0;
	k := 1;
	for i := 1 to cont do
	begin
		soma := soma + v[i];
		if soma > lim then
		begin
			w[k] := v[i];
			soma := 0;
			k := k + 1;
		end;
	end;
end;

begin
	insertV();
	readln(lim);
	insertW();
	for i := 1 to (k-1) do
		write(w[i], ' ');
end.