"use strict";(self.webpackChunkblessing_skin_server=self.webpackChunkblessing_skin_server||[]).push([[45],{8045:function(e,t,a){a.r(t);var n=a(2065),s=a(88),r=a(6703);const o=document.querySelector("#reset-avatar");null==o||o.addEventListener("click",(async function(){try{await(0,n.K)({text:(0,s.t)("user.resetAvatarConfirm")})}catch(e){return}const{message:e}=await(0,r.v_)("/user/profile/avatar",{tid:0});n.A.success(e),document.querySelectorAll('[alt="User Image"]').forEach((e=>{e.src=`${blessing.base_url}/avatar/0`}))}));const c=document.querySelector("#change-password");null==c||c.addEventListener("submit",(async function(e){e.preventDefault();const t=e.target,a=t.oldPassword.value,o=t.newPassword.value;if(o!==t.confirm.value)return n.A.error((0,s.t)("auth.invalidConfirmPwd")),void t.confirm.focus();const{code:c,message:i}=await(0,r.v_)("/user/profile?action=password",{current_password:a,new_password:o});await(0,n.K)({mode:"alert",text:i}),0===c&&(window.location.href=`${blessing.base_url}/auth/login`)}));const i=document.querySelector("#change-nickname");null==i||i.addEventListener("submit",(async function(e){e.preventDefault();const t=e.target.nickname.value,{code:a,message:s}=await(0,r.v_)("/user/profile?action=nickname",{new_nickname:t});(0,n.K)({mode:"alert",text:s}),0===a&&document.querySelectorAll('[data-mark="nickname"]').forEach((e=>{e.textContent=t}))}));const l=document.querySelector("#change-email");null==l||l.addEventListener("submit",(async function(e){e.preventDefault();const t=e.target,a=t.email.value,s=t.password.value,{code:o,message:c}=await(0,r.v_)("/user/profile?action=email",{email:a,password:s});await(0,n.K)({mode:"alert",text:c}),0===o&&(window.location.href=`${blessing.base_url}/auth/login`)}));const u=document.querySelector("#modal-delete-account");null==u||u.addEventListener("submit",(async function(e){e.preventDefault();const t=e.target.password.value,{code:a,message:s}=await(0,r.v_)("/user/profile?action=delete",{password:t});await(0,n.K)({mode:"alert",text:s}),0===a&&(window.location.href=blessing.base_url)}))}}]);