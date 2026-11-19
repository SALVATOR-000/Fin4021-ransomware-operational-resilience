// Usage: pdf2txt <input.pdf> <output.txt> [firstPage lastPage]
// Extracts the text layer with PDFKit, one block per PDF page, marked
// "=== PDF page N (printed label: X) ===". Page numbers are 1-based.
import Foundation
import PDFKit

let args = CommandLine.arguments
guard args.count >= 3 else {
    FileHandle.standardError.write("usage: pdf2txt in.pdf out.txt [first last]\n".data(using: .utf8)!)
    exit(2)
}
let inURL = URL(fileURLWithPath: args[1])
guard let doc = PDFDocument(url: inURL) else {
    FileHandle.standardError.write("cannot open \(args[1])\n".data(using: .utf8)!)
    exit(1)
}
var first = 1
var last = doc.pageCount
if args.count >= 5, let f = Int(args[3]), let l = Int(args[4]) { first = f; last = min(l, doc.pageCount) }
var out = ""
var emptyPages: [Int] = []
for i in (first - 1)..<last {
    guard let page = doc.page(at: i) else { continue }
    let label = page.label ?? ""
    let text = page.string ?? ""
    if text.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty { emptyPages.append(i + 1) }
    out += "\n\n=== PDF page \(i + 1)" + (label.isEmpty || label == String(i + 1) ? "" : " (printed label: \(label))") + " ===\n\n"
    out += text
}
try! out.write(to: URL(fileURLWithPath: args[2]), atomically: true, encoding: .utf8)
print("pages \(first)-\(last) of \(doc.pageCount); empty: \(emptyPages)")
