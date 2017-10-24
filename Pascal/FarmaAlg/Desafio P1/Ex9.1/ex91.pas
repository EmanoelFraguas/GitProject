program ex91;

var
peso, comidos: double;
cont, pomba: integer;

begin
	peso := 150;
	cont := 0;
	pomba := 16;
	while peso <= 100000000 do
	begin
		comidos := pomba * 900;
		peso := peso + ((peso * 0.9) * 300);
		cont := cont +1;
		pomba := pomba * 2;
	end;
	pomba := pomba div 2;
	writeln('A colheita ocorrerá em ',cont,' anos');
	writeln(pomba-16);
end.