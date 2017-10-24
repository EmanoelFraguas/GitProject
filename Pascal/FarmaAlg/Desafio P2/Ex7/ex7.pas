program ex7;

var
v1: array[1..100] of integer;
i, j, n, cont, media, aux: integer;
balance: boolean;

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
	cont := cont - 1;
end;

procedure order();
begin
	for j := 1 to cont-1 do
    begin
        for i := 2 to cont do
        begin
            if v1[i] < v1[i-1] then
            begin
                aux := v1[i-1];
                v1[i-1] := v1[i];
                v1[i] := aux;
            end;
        end;
    end;
end;

begin
	leitura();
	order();
	balance := true;
	media := v1[1] + v1[cont];
	for i := 1 to (cont div 2) do
	begin
		if (v1[i] + v1[cont - i + 1]) <> media then
		begin
			balance := false;
			break;
		end;
	end;
	if balance = true then
		writeln('Sim, eh balanceada.')
	else
		writeln('Nao eh balanceada.');
end.