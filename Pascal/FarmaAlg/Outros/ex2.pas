program ex2;

var
mat: array[1..3, 1..3] of integer;
aux: array[1..3, 1..3] of integer;
i, j: integer;

procedure printMat();

begin
	for j := 1 to 3 do
	begin
		for i := 1 to 3 do
			writeln(aux[i,j]);
	end;
end;

begin
	for j := 1 to 3 do
		for i := 1 to 3 do
			read(mat[i,j]);
	aux[1,1] := mat[1,3]; 	
	aux[1,2] := mat[2,3];
	aux[1,3] := mat[3,3];
	aux[2,1] := mat[1,2];
	aux[2,2] := mat[2,2];
	aux[2,3] := mat[3,2];
	aux[3,1] := mat[1,1];
	aux[3,2] := mat[2,1];
	aux[3,3] := mat[3,1];
	printMat();
end.