Summary:	Pretty-printer for converting C/C++ code to a LaTeX listing
Summary(pl.UTF-8):   Konwerter listingów C/C++ na LaTeX
Name:		C++2LaTeX
%define		ver	1_1pl1
Version:	1.1pl1
Release:	3
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.tex.ac.uk/tex-archive/support/%{name}-%{ver}.tar.gz
# Source0-md5:	439cf4f33983848f5d6761c6f605f631
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++2LaTeX takes as input a C or C++ source file and outputs a LaTeX
file that is a beautified listing (optionally the output can contain
the 'documentstyle' header and so on).

%description -l pl.UTF-8
C++2LaTeX przyjmuje na wejście kod źródłowy w C lub C++, a na wyjście
wysyła plik w LaTeXu z ładnym listingiem.

%prep
%setup -q -n %{name}-%{ver}

%build
rm -f *.o c++2latex
%{__make} \
	CFLAGS="%{rpmcflags} -DUSE_NAME"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install c++2latex	$RPM_BUILD_ROOT%{_bindir}
install c++2latex.1	$RPM_BUILD_ROOT%{_mandir}/man1
ln -sf c++2latex	$RPM_BUILD_ROOT%{_bindir}/c2latex
echo '.so c++2latex.1' >$RPM_BUILD_ROOT%{_mandir}/man1/c2latex.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
