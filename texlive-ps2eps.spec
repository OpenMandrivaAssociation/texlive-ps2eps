%global tl_name ps2eps
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.70
Release:	%{tl_revision}.1
Summary:	Produce Encapsulated PostScript from PostScript
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ps2eps
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2eps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ps2eps.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ps2eps.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Produce Encapsulated PostScript Files (EPS/EPSF) from a one-page
PostScript document, or any PostScript document. A correct Bounding Box
is calculated for the EPS files and some PostScript command sequences
that can produce erroneous results on printers are filtered. The input
is cropped to include just the image contained in the PostScript file.
The EPS files can then be included into TeX documents. Other programs
like ps2epsi (a script distributed with ghostscript) don't always
calculate the correct bounding box (because the values are put on the
PostScript stack which may get corrupted by bad PostScript code) or they
round it off, resulting in clipping the image. Therefore ps2eps uses a
resolution of 144 dpi to get the correct bounding box. The bundle
includes binaries for Linux, Solaris, Digital Unix or Windows
2000/9x/NT; for other platforms, the user needs perl, ghostscript and an
ANSI-C compiler. Included in the distribution is the bbox program, an
application to produce Bounding Box values for rawppm or rawpbm format
files.

