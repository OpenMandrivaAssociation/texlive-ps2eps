Name:		texlive-ps2eps
Version:	62856
Release:	2
Summary:	Produce Encapsulated PostScript from PostScript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ps2eps
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2eps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2eps.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Produce Encapsulated PostScript Files (EPS/EPSF) from a
one-page PostScript document, or any PostScript document. A
correct Bounding Box is calculated for the EPS files and some
PostScript command sequences that can produce errorneous
results on printers are filtered. The input is cropped to
include just the image contained in the PostScript file. The
EPS files can then be included into TeX documents. Other
programs like ps2epsi (a script distributed with ghostscript)
don't always calculate the correct bounding box (because the
values are put on the PostScript stack which may get corrupted
by bad PostScript code) or they round it off, resulting in
clipping the image. Therefore ps2eps uses a resolution of 144
dpi to get the correct bounding box. The bundle includes
binaries for Linux, Solaris, Digital Unix or Windows
2000/9x/NT; for other platforms, the user needs perl,
ghostscript and an ANSI-C compiler. Included in the
distribution is the bbox program, an application to produce
Bounding Box values for rawppm or rawpbm format files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/ps2eps
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ps2eps.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ps2eps.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bbox.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/bbox.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
