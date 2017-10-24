program ex5;

var
//Array primário
v1: array[1..1000] of integer;
v2: array[1..1000] of integer;
v3: array[1..1000] of integer;
i, j, k, n, cont, cont2, cont3, aux:integer;
tem: boolean;

procedure insertV1();
begin
	read(n);
	while n <> 0 do
	begin
		v1[cont] := n;
		read(n);
		cont := cont + 1;
	end;
	cont := cont - 1;
end;

procedure uniqueV2();
begin
	k := 1;
	for i := 1 to cont do
	begin
		tem := false;
		for j := 1 to cont do
			if v1[i] = v1[v2[j]] then
				tem := true;
		if tem = false then
		begin
			v2[k] := i;
			cont2 := cont2 + 1;
			k := k + 1;
		end;
	end;
end;

procedure repetidosV3();
begin
	k := 1;
	for i := 1 to cont do
	begin
		tem := false;
		for j := 1 to cont do
		begin
			if v2[j] <> 0 then
				if i = v2[j] then
					tem := true;
		end;
		if tem = false then
		begin
			v3[k] := i;
			cont3 := cont3 + 1;
			k := k + 1;
		end;
	end;
end;

procedure changeNum();
begin
	for i := 1 to cont do
	begin
		v2[i] := v1[v2[i]];
	end;
	for i := 1 to cont3 do
	begin
		v3[i] := v1[v3[i]];
	end;
end;

procedure orderV3();
begin
	for j := 1 to cont3 -1 do
    begin
        for i := 2 to cont3 do
        begin
            if v3[i] < v3[i-1] then
            begin
                aux := v3[i-1];
                v3[i-1] := v3[i];
                v3[i] := aux;
            end;
        end;
    end;
end;

procedure mergeMat();
begin
	for i := 1 to cont3 do
	begin		
			v2[i+cont2] := v3[i];
	end;
end;

// Aqui começa a porra do código
begin
	cont := 1;
	cont2 := 0;
	cont3 := 0;
	insertV1();
	uniqueV2();
	repetidosV3();
	changeNum();
	orderV3();
	mergeMat();	
	
	(*writeln('Numeros na matriz V1');
	for i := 1 to cont do
		write(v1[i], ' ');
	writeln('');
	writeln('Numeros dos indices V2');
	for i := 1 to cont2 do
		write(v2[i], ' ');
	writeln('');
	writeln('Numeros dos indices V3');
	for i := 1 to cont3 do
		write(v3[i], ' ');
	
	mergeMat();
	writeln('');
	writeln('Matriz final');*)
	for i := 1 to cont do
		write(v2[i], ' ');
end.