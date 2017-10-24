program ex9;

var
v1: array[1..100] of integer;
v2: array[1..50] of integer;
v3: array[1..50] of integer;
v4: array[1..50] of integer;
n1, n2, n3, i, j, k, l, m, n, cont, cont2, aux, maior, maiorCont, atualCont, result: integer;
ponte, tem: boolean;


//Le do tecladoe preenche o V1
procedure leitura();
begin
	read(n);
	cont := 1;
	while n <> 0 do
	begin
		v1[cont] := n;
		cont := cont + 1;
		read(n);
	end;
	v1[cont] := 999;
	//cont := cont - 1;
end;

//Coloca no v2 cada ocorrencia de repetiçao
procedure separa();
begin
	n1 := v1[1];
	n2 := v1[2];
	n3 := v1[3];
	k := 0;
	for i := 3 to cont do
	begin
		if (n1 = n2) and (n2 <> n3) then
		begin
			v2[k+1] := n2;
			k := k + 1;
		end;
		n1 := n2;
		n2 := n3;
		n3 := v1[i+1];
	end;
end;

//Ordena o v2 por ordem crescente
procedure order();
begin
	for j := 1 to k-1 do
    begin
        for i := 2 to k do
        begin
            if v2[i] < v2[i-1] then
            begin
                aux := v2[i-1];
                v2[i-1] := v2[i];
                v2[i] := aux;
            end;
        end;
    end;
end;

//Vezes que cada numero do V2 se repete (poe no v3);
procedure contagem();
begin
	for i := 1 to k do
		v3[i] := 1;
	l := 1;
	for i := 2 to k do
	begin
		if v2[i] = v2[i-1] then
			v3[l] := v3[l] + 1
		else
			l := l + 1;
	end;
end;

//Unifica a v2, deixando um numero de cada
procedure unique();
begin
	cont2 := 2;
	m := 1;
	for i:= 1 to k do
    begin
    	tem := false;
        for j := 1 to k do
        begin
            if v2[i] = v4[j] then
                tem := true;
        end;
        if tem = false then
        begin
            v4[m] := v2[i];
            cont2 := cont2 + 1;
			m := m + 1;
		end; 
    end;
end;

begin
	leitura();
	separa();
	order();
	contagem();
	unique();
	
	maior := v3[1];
	for i := 1 to l do
	begin
		if v3[i] > maior then
			maior := i;
	end;
	
	result := v4[maior];
	
	

	
	(*//Impressao para testes
	writeln('l: ', l);
	writeln('maior: ', maior);
	writeln('resultado: ', result);
	writeln('Repetidos');
	for i := 1 to k do
		write(v2[i], ' ');
	writeln('');
	writeln('Um de cada repetido');
	for i := 1 to (m-1) do
		write(v4[i], ' ');
	writeln('');
	writeln('Vezes que se repete');
	for i := 1 to l do
		write(v3[i], ' ');*)
	writeln(result);
end.