# PyCow修改版
## 修改内容
修改自github.com/p2k/PyCow，主要去除了Mootools的依赖，使之可以适应一般的Javascript平台，这个项目还很不完善，例如a,b = b,a这样的语句还不能很好的翻译。
## 新增内容
新增了一个Django的工程，可以快速的架设服务供其它软件使用，例如其在C#中的调用：
```csharp
public static string py2js(string pycode) {
    try {
        HttpWebRequest request;
        request = (HttpWebRequest)WebRequest.Create(
             JavaScriptEngine.getContext().GetParameter("py2js_uri") as string
        );
        request.Timeout = 30000;// 30s for timeout
        request.Method = "POST";
        byte[] postData = Encoding.UTF8.GetBytes(string.Format("q={0}", Convert.ToBase64String(Encoding.UTF8.GetBytes(pycode))));
        request.ContentType = "application/x-www-form-urlencoded";
        request.ContentLength = postData.Length;
        Stream postStream = request.GetRequestStream();
        postStream.Write(postData, 0, postData.Length);
        postStream.Close();
        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        StreamReader myreader = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
        string jscode = myreader.ReadToEnd();
        myreader.Close();
        return jscode;
    } catch (Exception e) {
        Logger.logWarn("HTTP error (@py2js):" + e.Message);
        return "内部错误:" + e.Message;
    }
}
```