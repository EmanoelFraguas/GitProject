program ex4;

var
v1: array [1..20] of integer;
v2: array [1..20] of integer;
i, j, n, num, cont, corCerta, corErrada: integer;
tem: boolean;

function uniquev1(num: integer): boolean;
begin
	uniquev1 := false;
	for j := 1 to 20 do
	begin
		if v1[j] = num then
		begin
			uniquev1 := true;
		end;
	end;
end;

function uniquev2(num: integer): boolean;
begin
	uniquev2 := false;
	for j := 1 to 20 do
	begin
		if v2[j] = num then
		begin
			uniquev2 := true;
		end;
	end;
end;

procedure insertVet1();
begin
	//writeln('Escreva o range maximo:');
	read(n);
	for i := 1 to n do
	begin
		//writeln('Escreva um numero:');
		readln(num);
		tem := uniquev1(num);
		while (num < 1) or (num > 30) or (tem = true) do
		begin
			//writeln('O numero digitado ja existe. Digite outro:');
			readln(num);
			tem := uniquev1(num);
		end;
		v1[i] := num;
	end;
end;

procedure insertVet2();
begin
	for i := 1 to n do
	begin
		//writeln('Escreva um numero:');
		readln(num);
		//tem := uniquev2(num);
		while (num < 1) or (num > 30) (*or (tem = true)*) do
		begin
			//writeln('O numero digitado ja existe. Digite outro:');
			readln(num);
			//tem := uniquev2(num);
		end;
		v2[i] := num;
	end;
end;

function certa(): integer;
begin
	corCerta := 0;
	for i := 1 to n do
	begin
		if v1[i] = v2[i] then
			corCerta := corCerta + 1;
	end;
	certa := corCerta;
end;

function errada(): integer;
begin	
	corErrada := 0;
	for j := 1 to n do
	begin
		tem := false;
		for i := 1 to n do
		begin
			if v2[j] = v1[i] then
			begin
				tem := true;
				break;
			end;
		end;
		if tem = true then
		begin
			if v2[j] <> v1[j] then
				corErrada := corErrada + 1;
		end;
	end;
	errada := corErrada;
end;

begin
	insertVet1();
	corCerta := 0;
	corErrada := 0;
	cont := 0;
	while (corCerta <> n) or (corErrada <> 0) do
	begin
		//writeln('entrou');
		insertVet2();
		corCerta := certa();
		write('Cores no lugar certo: ', corCerta);
		corErrada := errada();
		writeln(', cores no lugar errado: ', corErrada, '.');
		cont := cont + 1;
	end;
	writeln('Foram lidos ', cont, ' vetores.');
	
	
	(*writeln('V1');
	for i := 1 to n do
		write(v1[i], ' ');
	writeln('');
	writeln('V2');
	for i := 1 to n do
		write(v2[i], ' *)
end.