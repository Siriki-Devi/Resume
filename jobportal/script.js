// REGISTER
if (registerBtn) {
registerBtn.onclick = () => {
localStorage.setItem("user", JSON.stringify({
name: name.value,
email: email.value,
password: password.value
}));
alert("Registered");
location.href = "index.html";
};
}

// LOGIN
if (loginBtn) {
loginBtn.onclick = () => {
if (loginRole.value === "admin") {
if (loginEmail.value === "admin@gmail.com" && loginPassword.value === "admin123") {
location.href = "admin.html";
} else alert("Invalid Admin");
} else {
let u = JSON.parse(localStorage.getItem("user"));
if (u && u.email === loginEmail.value && u.password === loginPassword.value) {
localStorage.setItem("loggedUser", u.email);
location.href = "jobs.html";
} else alert("Invalid User");
}
};
}

// ADD JOB
if (addJobBtn) {
addJobBtn.onclick = () => {
let jobs = JSON.parse(localStorage.getItem("jobs")) || [];
jobs.push({
title: jobTitle.value,
company: companyName.value,
location: jobLocation.value,
package: jobPackage.value,
skills: jobSkills.value,
desc: jobDesc.value
});
localStorage.setItem("jobs", JSON.stringify(jobs));
alert("Job Added");
location.reload();
};
}

// SHOW JOBS
if (jobTable) {
(JSON.parse(localStorage.getItem("jobs")) || []).forEach((j,i)=>{
jobTable.innerHTML += `
<tr>
<td>${j.title}</td>
<td>${j.company}</td>
<td>${j.location}</td>
<td>${j.package}</td>
<td><button onclick="applyJob(${i})">Apply</button></td>
</tr>`;
});
}
function applyJob(i){
localStorage.setItem("jobIndex", i);
location.href="applyform.html";
}

// APPLY FORM
if (applyForm) {
applyForm.onsubmit=e=>{
e.preventDefault();
let reader=new FileReader();
reader.onload=()=>{
let apps=JSON.parse(localStorage.getItem("appliedJobs"))||[];
let jobs=JSON.parse(localStorage.getItem("jobs"));
let job=jobs[localStorage.getItem("jobIndex")];
apps.push({
user: localStorage.getItem("loggedUser"),
name: fullName.value,
email: email.value,
job: job.title,
company: job.company,
resume: reader.result
});
localStorage.setItem("appliedJobs",JSON.stringify(apps));
alert("Applied");
location.href="jobs.html";
};
reader.readAsDataURL(resume.files[0]);
};
}

// USER VIEW APPLIED
if (appliedTable) {
(JSON.parse(localStorage.getItem("appliedJobs"))||[])
.filter(a=>a.user===localStorage.getItem("loggedUser"))
.forEach((a,i)=>{
appliedTable.innerHTML+=`
<tr>
<td>${a.job}</td>
<td>${a.company}</td>
<td><a href="${a.resume}" target="_blank">View</a></td>
<td><button onclick="del(${i})">Delete</button></td>
</tr>`;
});
}
function del(i){
let a=JSON.parse(localStorage.getItem("appliedJobs"));
a.splice(i,1);
localStorage.setItem("appliedJobs",JSON.stringify(a));
location.reload();
}

// ADMIN VIEW APPLIED
if (adminApplied) {
(JSON.parse(localStorage.getItem("appliedJobs"))||[])
.forEach(a=>{
adminApplied.innerHTML+=`
<tr>
<td>${a.name}</td>
<td>${a.email}</td>
<td>${a.job}</td>
<td><a href="${a.resume}" target="_blank">View Resume</a></td>
</tr>`;
});
}

// ADMIN JOB LIST
if (adminJobTable) {
(JSON.parse(localStorage.getItem("jobs"))||[]).forEach((j,i)=>{
adminJobTable.innerHTML+=`
<tr>
<td>${j.title}</td>
<td>${j.company}</td>
<td>${j.location}</td>
<td>${j.package}</td>
<td>${j.skills}</td>
<td><button onclick="delJob(${i})">Delete</button></td>
</tr>`;
});
}
function delJob(i){
let j=JSON.parse(localStorage.getItem("jobs"));
j.splice(i,1);
localStorage.setItem("jobs",JSON.stringify(j));
location.reload();
}

// NAV
function logout(){localStorage.removeItem("loggedUser");location.href="index.html";}
function goBack(){history.back();}
