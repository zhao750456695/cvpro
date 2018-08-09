<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>基本信息_考研帮</title>
<link rel="stylesheet" type="text/css" href="//i.kaoyan.com/style/css/v1pub.css?v=201510093"/>
<link rel="stylesheet" type="text/css" href="//i.kaoyan.com/style/css/setting.css?v=201510093" />
<script type="text/javascript" src="//i.kaoyan.com/style/js/jquery-1.11.2.min.js?v=201510093"></script>
<script type="text/javascript" src="//i.kaoyan.com/style/js/util.js?v=201510093"></script>
<script type="text/javascript" src="//i.kaoyan.com/style/js/form.js?v=201510093"></script>
<script type="text/javascript" src="//i.kaoyan.com/style/js/city.js?v=201510093"></script>
<script type="text/javascript" src="//i.kaoyan.com/style/3td/school/sch.js?v=201510093"></script>
<link rel="stylesheet" type="text/css" href="//i.kaoyan.com/style/3td/artDialog/ui-dialog.css?v=201510093" />
<script type="text/javascript" src="//i.kaoyan.com/style/3td/artDialog/dialog-min.js?v=201510093"></script>
<script type="text/javascript">
  jQuery(function(){
    $('li[xd-class="hover"]').hover(function(){
        $(this).children('a').addClass('hover');
        $(this).children('dl').show();
    },function(){
        $(this).children('a').removeClass('hover');
        $(this).children('dl').hide();
    });
});
</script>
</head>
<body>

<!--top begin-->
<div class="header">
    <div class="gtop">
        <div class="dh">
          <div class="plogo"><a href="//i.kaoyan.com/"><img src="//i.kaoyan.com/style/img/ky_logo.png" height="40" /></a></div>
          <ul class="pmenu fleft f14">
            <li><a href="http://www.kaoyan.com/" class="link">首页</a></li>
            <li><a href="http://bang.kaoyan.com/" class="link">考研帮</a></li>
            <li><a href="http://bbs.kaoyan.com/" class="link">论坛</a></li>
            <li><a href="http://www.bangxuetang.com/" class="link">学堂</a></li>
          </ul>
                      <ul class="pmenu fright">
              <li xd-class="hover">
                  <a href="//i.kaoyan.com/" class="link">
                    <img id='x-avatar' src="//i.kaoyan.com/avatar/pic.png" alt="头像" width="30" class="avatar"/>
                    <span>bingfenghaol</span>
                    <i class="icon iconfont icon-zhankai"></i>
                  </a>
                  <dl class="pchild" style="width:133px;">
                      <dd><a href="//i.kaoyan.com/set/">个人设置</a></dd>
                      <dd><a href="//i.kaoyan.com/logout">退出</a></dd>
                  </dl>
              </li>
            </ul>
                  </div>
    </div>
</div>
<!--top end-->

<!--content begin-->
<div class="gdiv dh">
    <div class="my_menu">
    <h3>设置中心</h3>
    <dl class="list">
        <dt class="c1"><i class="icon iconfont icon-home"></i><span>个人设置</span></dt>
        <dd id="setting_profile"><a href="//i.kaoyan.com/set/profile">基本信息</a></dd>
        <dd id="setting_address"><a href="//i.kaoyan.com/set/address">收货地址</a></dd>
    </dl>
    <dl class="list">
        <dt id="setting_avatar" class="c2"><a href="//i.kaoyan.com/set/avatar"><i class="icon iconfont icon-pen"></i><span>修改头像</span></a></dt>
    </dl>
    <dl class="list">
        <dt id="setting_bind" class="c3"><a href="//i.kaoyan.com/set/bind"><i  class="icon iconfont icon-link"></i><span>账户绑定</span></a></dt>
    </dl>
    <dl class="list">
        <dt id="setting_safe" class="c4"><i  class="icon iconfont icon-anquan"></i><span>账户安全</span></dt>
        <dd id="setting_password"><a href="//i.kaoyan.com/set/password">修改密码</a></dd>
        <dd id="setting_email"><a href="//i.kaoyan.com/set/email">邮箱认证</a></dd>
        <dd id="setting_phone"><a href="//i.kaoyan.com/set/phone">手机绑定</a></dd>
    </dl>
</div>
<script type="text/javascript">
var _mu=$('#setting_profile').addClass('ok');
if (_mu.is('dd')) {
    _mu.siblings('dt').addClass('ok');
};
</script>

    <div class="my_main">
        <div class="title">
            <h2>个人设置 <span>(<em>*</em> 必須填写项)</span></h2>
            <p>以下信息将显示在个人资料页，方便大家了解你。</p>
        </div>

        <div>
            <form id="proform" method="post">
              <input type="hidden" name="isdone" value="1">
              <table cellspacing="0" cellpadding="0" class="tbform" align="center">
                <tbody>
                  <tr>
                    <th width="120">您的登录用户名：</th>
                    <td> bingfenghaol (<a href="//i.kaoyan.com/set/password">修改密码</a>) </td>
                  </tr>
                  <tr>
                    <th>真实姓名：</th>
                    <td><input type="text" class="tinp" name="realname" value="赵晓杰"></td>
                  </tr>
                  <tr>
                    <th><i>*</i>性别：</th>
                    <td class="vam f14">
                          <label class="radio"><input emel="sexem" class="sex" value="1" name="sex" type="radio"> 男</label>&nbsp;&nbsp;&nbsp;&nbsp;<label class="radio"><input emel="sexem" class="sex" value="2" name="sex" type="radio"> 女</label>
                          <span class="tip" id="sexTip"></span>
                          <script type="text/javascript">FXD.setInput('.sex','1');</script>  
                    </td>
                  </tr>
                  <tr>
                    <th><i>*</i>考研年份：</th>
                    <td class="vam f14">
                        <select id="x-year" name="year" class="reg-select">
                            <option value="0">请选择</option>
                                                                                        <option value="2017">2017年</option>
                                                            <option value="2018">2018年</option>
                                                            <option value="2019">2019年</option>
                                                            <option value="2020">2020年</option>
                                                            <option value="2021">2021年</option>
                                                    </select>
                        <span class="tip" id="x-yearTip"></span>
                        <script type="text/javascript">FXD.setInput('#x-year','2020');</script>
                    </td>
                  </tr>
                  <tr>
                    <th><i>*</i>本科院校：</th>
                    <td>
                        <input id="x-preschid" type="hidden" class="tinp" name="preschid" value="1008">
                        <input readonly="readonly" type="text" class="tinp schsec" name="preschname" value="中国原子能科学研究院">
                        <span class="tip" id="x-preschidTip"></span>
                    </td>
                  </tr>

                  <tr>
                    <th><i>*</i>目标院校：</th>
                    <td>
                        <input id="x-schid" type="hidden" class="tinp" name="schid" value="1000">
                        <input readonly="readonly" type="text" class="tinp schsec" name="schname" value="清华大学">
                        <span class="tip" id="x-schidTip"></span>
                    </td>
                  </tr>
                  <tr>
                    <th>备选1目标院校：</th>
                    <td>
                        <input type="hidden" class="tinp" name="schid1" value="">
                        <input readonly="readonly" type="text" class="tinp schsec" name="schname1" value="">
                        <a href="javascript:;" onclick="clearSecValue(this)">清除</a>
                    </td>
                  </tr>
                  <tr>
                    <th>备选2目标院校：</th>
                    <td>
                        <input type="hidden" class="tinp" name="schid2" value="">
                        <input readonly="readonly" type="text" class="tinp schsec" name="schname2" value="">
                        <a href="javascript:;" onclick="clearSecValue(this)">清除</a>
                    </td>
                  </tr>
                  <tr>
                    <th><i>*</i>报考专业：</th>
                    <td>
                        <input id="x-speid" type="hidden" class="tinp" name="speid" value="10020102">
                        <input readonly="readonly" type="text" class="tinp majsec" name="spename" value="经济思想史">
                        <span class="tip" id="x-speidTip"></span>
                    </td>
                  </tr>
                  <tr>
                    <th><i>*</i>所在地：</th>
                    <td>
                        <select id="x-proid" name="proid" class="reg-select" value="2471"><option value="0">请选择</option></select>
                        <select id="x-cityid" name="cityid" class="reg-select" value="2609"><option value="0">请选择</option></select>
                        <input type="text" id="CY_txt" name="subcity" style="display:none;">
                        <span class="tip" id="x-cityidTip"></span>
                    </td>
                  </tr>

                  <tr>
                    <th>个人简介：</th>
                    <td><textarea class="tixt" name="intro"></textarea></td>
                  </tr>
                  <tr>
                    <th height="60">&nbsp;</th>
                    <td><button id="probtn" class="btnbg btn1" type="submit">保存</button></td>
                  </tr>
                </tbody>
              </table>
            </form>
        </div>

    </div>
</div>
<!--content end-->

<script type="text/javascript">
// 清理数据
function clearSecValue(A){
    $(A).prev('input').val('');
}
// 选择学校
$('.schsec').XDSchInit(function(data,o){
  $(o).val(data.name);
  $(o).prev('input[type=hidden]').val(data.id).trigger('blur');
  return true;
});
// 选择专业
$('.majsec').XDMajInit(function(data,o){
  $(o).val(data.name);
  $(o).prev('input[type=hidden]').val(data.id).trigger('blur');
  return true
});

// 提交FORM
$('#proform').XDFormInit({ submit:"probtn",ajax:true,startFunc:function(v){
    $('#probtn').attr('disabled',true).text('保存中...');
},doneFunc:function(data){
    FXD.btnLock('#probtn',3,data.state>=1 ? '保存成功' : '保存失败','保存');
} });
$('input[name=sex]').XDFormInput({ msgId:'sexTip' });
$('#x-year').XDFormInput({ onFocus:"请选择考研年份", onError:'考研年份不能为空' });
$('#x-preschid').XDFormInput({ onFocus:"请选择本科院校", onError:'本科院校不能为空',zero:true });
$('#x-schid').XDFormInput({ onFocus:"请选择目标院校", onError:'目标院校不能为空',zero:true });
$('#x-speid').XDFormInput({ onFocus:"请选择报考专业", onError:'报考专业不能为空',zero:true });
$('#x-cityid').XDFormInput({ onFocus:"请选择地区", func:function(v){ return v==='0' ? false : true; } });
$.CYinit({ prov:'x-proid',city:'x-cityid' });
</script>



<!--bottom begin-->
<div class="gfoot dh">
    <a href="http://www.kaoyan.com/">考研网</a> Copyright &copy; 2015 kaoyan.com, all rights reserved 京ICP备09032638号
</div>
<!--bottom end-->

</body>
</html>