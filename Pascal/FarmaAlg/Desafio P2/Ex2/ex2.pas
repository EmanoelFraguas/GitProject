program ex2;

var
v1: array[1..106] of Char;
pos, dir, spaces, ann, i, j,cont, loops: integer;
done: boolean;

procedure preencheVetor();
begin
	read(spaces, ann);
	for i := 1 to spaces do
		v1[i] := '_';
	for i := 1 to ann do
	begin
		read(pos, dir);
		if dir = 1 then
			v1[pos] := '>'
		else if dir = - 1 then
			v1[pos] := '<';
	end;
end;

procedure termino();
begin
	done := true;
	for j := 1 to spaces do
	begin
		if v1[j] <> '_' then
		begin
			done := false
		end;
	end;
end;

begin	
	preencheVetor();
	for i := 1 to spaces do
		write(v1[i]);
	writeln('');
		
	(*for j := 1 to spaces do
		write(v1[j]);
	writeln('');*)	
	done := false;
	loops := 1;
	while done = false do
	begin
		cont := 1;
		while cont <= spaces do
		begin
			if (cont = 1) and (v1[1] = '<') then
				v1[1] := '_'	
			else if (v1[spaces] = '>') and (cont = spaces) then
				v1[spaces] := '_'
			else if (v1[cont] = '<') and (v1[cont-1] <> '_') then
				v1[cont] := '>'
			else if (v1[cont] = '>') and (v1[cont+1] <> '_') then
				v1[cont] := '<'
			else if (v1[cont] = '>') and (v1[cont+1] = '_') then
			begin
				v1[cont] := '_';
				v1[cont+1] := '>';
				cont := cont + 1;
			end
			else if (v1[cont] = '<') and (v1[cont-1] = '_') then
			begin
				v1[cont] := '_';
				v1[cont-1] := '<';
			end;
			cont := cont + 1;			
		end;
		for i := 1 to spaces do
			write(v1[i]);
		writeln('');
	
		termino();
		loops := loops + 1;
	end;
	writeln(loops);
end.