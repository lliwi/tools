/**
 * This script automatically generates OperationConfig.json, containing metadata
 * for each operation in the src/core/operations directory.
 * It also generates modules in the src/core/config/modules directory to separate
 * out operations into logical collections.
 *
 * @author n1474335 [n1474335@gmail.com]
 * @copyright Crown Copyright 2018
 * @license Apache-2.0
 */

/* eslint no-console: ["off"] */

import path from "path";
import fs  from "fs";
import process from "process";
import * as Ops from "../../operations/index.mjs";

const dir = path.join(process.cwd() + "/src/core/config/");
if (!fs.existsSync(dir)) {
    console.log("\nCWD: " + process.cwd());
    console.log("Error: generateConfig.mjs should be run from the project root");
    console.log("Example> node --experimental-modules src/core/config/scripts/generateConfig.mjs");
    process.exit(1);
}


const operationConfig = {},
    modules = {};

/**
 * Generate operation config and module lists.
 */
for (const opObj in Ops) {
    const op = new Ops[opObj]();

    operationConfig[op.name] = {
        module:      op.module,
        description: op.description,
        infoURL:     op.infoURL,
        inputType:   op.inputType,
        outputType:  op.presentType,
        flowControl: op.flowControl,
        manualBake:  op.manualBake,
        args:        op.args,
        checks:      op.checks
    };

    if (!(op.module in modules))
        modules[op.module] = {};
    modules[op.module][op.name] = opObj;
}


/**
 * Write OperationConfig.
 */
fs.writeFileSync(
    path.join(dir, "OperationConfig.json"),
    JSON.stringify(operationConfig, null, 4)
);
console.log("Written OperationConfig.json");


/**
 * Write modules.
 */
if (!fs.existsSync(path.join(dir, "modules/"))) {
    fs.mkdirSync(path.join(dir, "modules/"));
}

for (const module in modules) {
    let code = `/**
* THIS FILE IS AUTOMATICALLY GENERATED BY src/core/config/scripts/generateConfig.mjs
*
* @author n1474335 [n1474335@gmail.com]
* @copyright Crown Copyright ${new Date().getUTCFullYear()}
* @license Apache-2.0
*/
`;

    for (const opName in modules[module]) {
        const objName = modules[module][opName];
        code += `import ${objName} from "../../operations/${objName}.mjs";\n`;
    }

    code += `
const OpModules = typeof self === "undefined" ? {} : self.OpModules || {};

OpModules.${module} = {
`;
    for (const opName in modules[module]) {
        const objName = modules[module][opName];
        code += `    "${opName}": ${objName},\n`;
    }

    code += `};

export default OpModules;
`;
    fs.writeFileSync(
        path.join(dir, `modules/${module}.mjs`),
        code
    );
    console.log(`Written ${module} module`);
}


/**
 * Write OpModules wrapper.
 */
let opModulesCode = `/**
* THIS FILE IS AUTOMATICALLY GENERATED BY src/core/config/scripts/generateConfig.mjs
*
* Imports all modules for builds which do not load modules separately.
*
* @author n1474335 [n1474335@gmail.com]
* @copyright Crown Copyright ${new Date().getUTCFullYear()}
* @license Apache-2.0
*/
`;

for (const module in modules) {
    opModulesCode += `import ${module}Module from "./${module}.mjs";\n`;
}

opModulesCode += `
const OpModules = {};

Object.assign(
    OpModules,
`;

for (const module in modules) {
    opModulesCode += `    ${module}Module,\n`;
}

opModulesCode += `);

export default OpModules;
`;

fs.writeFileSync(
    path.join(dir, "modules/OpModules.mjs"),
    opModulesCode
);
console.log("Written OpModules.mjs");
