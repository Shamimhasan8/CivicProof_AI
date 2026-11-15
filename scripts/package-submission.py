from pathlib import Path
import zipfile
root=Path(__file__).resolve().parents[1]
out=root/'public'/'reports'/'CivicProof_Submission_Package.zip'
skip={'.git','node_modules','dist','.next','.vinext','.wrangler','.sites-runtime','tmp','outputs','work','.codex','.agents'}
allowed_dirs={'app','components','lib','worker','db','drizzle','migrations','hooks','scripts','tests','docs','public','vendor','.openai'}
allowed_root={'.gitignore','.npmrc','.env.example','package.json','package-lock.json','tsconfig.json','next.config.ts','vite.config.ts','postcss.config.mjs','eslint.config.mjs','components.json','drizzle.config.ts','cloudflare-env.d.ts'}
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for path in sorted(root.rglob('*')):
        rel=path.relative_to(root)
        if not path.is_file() or any(p in skip for p in rel.parts) or path==out:continue
        if not (rel.parts[0] in allowed_dirs or (len(rel.parts)==1 and (path.suffix=='.md' or path.name in allowed_root))):continue
        if path.name.startswith('.env') and path.name!='.env.example':continue
        if path.suffix in {'.pem','.key','.tsbuildinfo'}:continue
        z.write(path,'CivicProof_AI/'+str(rel))
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    names=z.namelist()
    for needed in ['app/page.tsx','lib/civic/engine.mjs','tests/evaluate.mjs','.env.example','README.md','VIDEO_SCRIPT.md','SUBMISSION.md']:
        assert 'CivicProof_AI/'+needed in names,needed
    print('Submission archive:',len(names),'files;',out.stat().st_size,'bytes')
