program q2;

var
v:array[1..100] of real;
n, soma, u, dsv: real;
i, cont: integer;

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

function fartocel(var far:real):real;
begin
	fartocel := ((5 * (far - 32))/9);
end;

procedure insertCel();
begin
	for i := 1 to cont do
	begin
		v[i] := fartocel(v[i]);
	end;
end;

function media(): real;
begin
	soma := 0;
	for i:= 1 to cont do
	begin
		soma := soma + v[i];
	end;
	media := soma/cont;
end;

function desvioP(u: real):real;
begin
	soma := 0;
	for i := 1 to cont do
	begin
		soma := soma + ((v[i]-u)*(v[i]-u));
	end;
	desvioP := sqr(soma/cont);
end;

begin
	insertV();
	insertCel();
	u := media();
	dsv := desvioP(u);
	writeln('A media eh ',u:0:3,' e o desvio eh ',dsv:0:3)
end.