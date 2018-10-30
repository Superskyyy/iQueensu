console.log("postbuild started");
const fs = require('fs-extra');
const module_name = "qhome"
const app_name = "indexPage"
const relative_output_static = "../../" + app_name + "/static/" + app_name + "/static/"
const relative_output_template = "../../" + app_name + "/templates/" + app_name + "/" + module_name + "/"
fs.mkdirp(relative_output_static, function (err) {
  if (err) {
    console.log('fails creating static folder')
    console.error(err);
  } else {
    console.log('created output static folder')
  }
});
fs.mkdirp(relative_output_template, function (err) {
  if (err) {
    console.log('fails creating template folder')
    console.error(err);
  } else {
    console.log('created output template folder')
  }
});
fs.emptyDirSync(relative_output_static);
fs.copy("build/index.html", relative_output_template + module_name + ".html");
fs.copySync("build/static/", relative_output_static);
