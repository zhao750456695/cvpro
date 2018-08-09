if($('secqaa_qS0')) {
	var sectpl = seccheck_tpl['qS0'] != '' ? seccheck_tpl['qS0'].replace(/<hash>/g, 'codeqS0') : '';
	var sectplcode = sectpl != '' ? sectpl.split('<sec>') : Array('<br />',': ','<br />','');
	var string = '<input name="secqaahash" type="hidden" value="qS0" />' + sectplcode[0] + '验证问答' + sectplcode[1] + '<input name="secanswer" id="secqaaverify_qS0" type="text" autocomplete="off" style="width:100px" class="txt px vm" onblur="checksec(\'qaa\', \'qS0\')" />' +
		' <a href="javascript:;" onclick="updatesecqaa(\'qS0\');doane(event);" class="xi2">换一个</a>' +
		'<span id="checksecqaaverify_qS0"><img src="' + STATICURL + 'image/common/none.gif" width="16" height="16" class="vm" /></span>' +
		sectplcode[2] + '五*20=?' + sectplcode[3];
	evalscript(string);
	$('secqaa_qS0').innerHTML = string;
}