var r = null;
//用于递归查询子模型
export function searchObject(object, name, className = null, TypeName = null) {
    var result = object;
    if (className != null) {
        let flag = false;
        object.children.forEach(item => {
            if (item.name == name) {
                return item;
            }
            if (item.name == className) {
                result = item;
                flag = true;
            }
        });
        if (!flag) {
            return null;
        }
    }
    if (TypeName != null) {
        let flag = false;
        result.children.forEach(item => {
            if (item.name == name) {
                return item;
            }
            if (item.name == className) {
                result = item;
                flag = true;
            }
        });
        if (!flag) {
            return null;
        }
    }
    dfs(result, name);
    return r;
}

function dfs(object, name) {
    if (object.name == name) {
        r = object;
    }
    object.children.forEach(item => {
        dfs(item, name);
    });
}