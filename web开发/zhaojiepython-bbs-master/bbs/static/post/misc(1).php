if($('seccode_cS0')) {
	if(!$('vseccode_cS0')) {
		var sectpl = seccheck_tpl['cS0'] != '' ? seccheck_tpl['cS0'].replace(/<hash>/g, 'codecS0') : '';
		var sectplcode = sectpl != '' ? sectpl.split('<sec>') : Array('<br />',': ','<br />','');
		var string = '<input name="seccodehash" type="hidden" value="cS0" /><input name="seccodemodid" type="hidden" value="forum::post" />' + sectplcode[0] + '验证码' + sectplcode[1] + '<input name="seccodeverify" id="seccodeverify_cS0" type="text" autocomplete="off" style="ime-mode:disabled;width:100px" class="txt px vm" onblur="checksec(\'code\', \'cS0\', 0, null, \'forum::post\')" />' +
			' <a href="javascript:;" onclick="updateseccode(\'cS0\');doane(event);" class="xi2">换一个</a>' +
			'<span id="checkseccodeverify_cS0"><img src="' + STATICURL + 'image/common/none.gif" width="16" height="16" class="vm" /></span>' +
			sectplcode[2] + '<span id="vseccode_cS0"> <img onclick="updateseccode(\'cS0\')" width="100" height="30" src="misc.php?mod=seccode&update=48986&idhash=cS0" class="vm" alt="" /></span>' + sectplcode[3];
		evalscript(string);
		$('seccode_cS0').innerHTML = string;
	} else {
		var string = ' <img onclick="updateseccode(\'cS0\')" width="100" height="30" src="misc.php?mod=seccode&update=48986&idhash=cS0" class="vm" alt="" />';
		evalscript(string);
		$('vseccode_cS0').innerHTML = string;
	}
	
}