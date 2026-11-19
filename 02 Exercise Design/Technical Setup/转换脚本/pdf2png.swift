// Usage: pdf2png <input.pdf> <output dir> <name prefix> [width px, default 1100]
// Renders every page of a PDF to "<prefix> page N.png" (white background). Used for scanned PDFs with no text layer.
import Foundation
import PDFKit
import AppKit

let a = CommandLine.arguments
guard a.count >= 4, let doc = PDFDocument(url: URL(fileURLWithPath: a[1])) else { FileHandle.standardError.write("usage: pdf2png in.pdf outdir prefix [width]\n".data(using: .utf8)!); exit(2) }
let width = a.count >= 5 ? (Double(a[4]) ?? 1100) : 1100
for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let box = page.bounds(for: .mediaBox)
    let scale = CGFloat(width) / box.width
    let w = Int(box.width * scale), h = Int(box.height * scale)
    guard let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0),
          let ctx = NSGraphicsContext(bitmapImageRep: rep) else { continue }
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = ctx
    ctx.cgContext.setFillColor(NSColor.white.cgColor)
    ctx.cgContext.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.cgContext.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ctx.cgContext)
    NSGraphicsContext.restoreGraphicsState()
    let out = URL(fileURLWithPath: a[2]).appendingPathComponent("\(a[3]) page \(i + 1).png")
    try! rep.representation(using: .png, properties: [:])!.write(to: out)
    print("wrote \(out.lastPathComponent) \(w)x\(h)")
}
