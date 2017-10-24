program ex6;

var
mat: array[1..10,1..10] of integer;
aux: array[1..10,1..10] of integer;
i, j: integer;

procedure readMat();

begin
	for j := 1 to 10 do
		for i := 1 to 10 do
			read(mat[i,j]);
end;

procedure printMat();

begin
	for j := 1 to 10 do
		for i := 1 to 10 do
			writeln(mat[i,j]);
end;

procedure doisxoito();
begin
	for i := 1 to 10 do
	begin
		aux[2,i] := mat[2,i];
		mat[2,i] := mat[8,i];
		mat[8,i] := aux[2,i];
	end;	
end;

procedure quatroxdez();
begin
	for i := 1 to 10 do
	begin
		aux[i,4] := mat[i,4];
		mat[i,4] := mat[i,10];
		mat[i,10] := aux[i,4];
	end;	
end;

procedure diagonais1();

begin
	for j := 1 to 10 do
		for i := 1 to 10 do
			aux[i,j] := mat[i,j];
	for i := 1 to 10 do
	begin
		mat[i,i] := aux[i,11-i];
		mat[i,11-i] := aux[i,i];           
	end;
end;

procedure diagonais2();

begin
	for j := 1 to 10 do
		for i := 1 to 10 do
			aux[i,j] := mat[i,j];
	for i := 1 to 10 do
	begin
		mat[i,i] := aux[11-i,i];
		mat[11-i,i] := aux[i,i];           
	end;
end;

begin
	readMat();
	doisxoito();
	quatroxdez();
	diagonais1();
	//diagonais2();
	printMat();
end.