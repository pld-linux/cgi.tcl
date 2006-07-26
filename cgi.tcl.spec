%define		_mainver	1.8
Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(pl):	Tool Command Language - jêzyk skryptowy z bibliotekami dynamicznymi
Name:		cgi.tcl
Version:	1.8.0
Release:	1
License:	Public Domain
Group:		Development/Languages/Tcl
Source0:	http://expect.nist.gov/%{name}/cgi.tcl.tar.gz
# Source0-md5:	51aa4cbcd401d760a7c5621c28b78125
Patch0:		%{name}-DESTDIR.patch
URL:		http://expect.nist.gov/cgi.tcl/
BuildRequires:	autoconf
BuildRequires:	tcl
Requires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_packagedir	%{_libdir}/tcl8.3/cgi%{_mainver}

%description
cgi.tcl is the CGI support library for Tcl programmers. The library is
very thorough - it supports forms, tables, cookies, file upload,
plug-ins, JavaScript, Netscape extensions, etc, etc. It also provides
very convenient support for debugging and handling CGI errors. cgi.tcl
can also be used for generating static HTML. This enables you to get
programming features into HTML, such as variables, if/then/else, file
I/O, etc. For example, HTML lacks variables so if you repeatedly use a
link on a page and one day the link changes, you've got to update
every use of the link, possibly on hundreds of pages. By storing the
link in a Tcl variable, you can just change the one place where the
variable is defined. This makes maintenance much easier. This is just
a tiny example of the benefits cgi.tcl provides.

%description -l pl
cgi.tcl to biblioteka obs³ugi CGI dla programistów Tcl. Biblioteka ma
du¿± funkcjonalno¶æ - obs³uguje formularze, tabelki, ciasteczka,
upload plików, wtyczki, JavaScript, rozszerzenia Netscape itp.
Udostêpnia tak¿e bardzo wygodne wsparcie dla odpluskwiania i obs³ugi
b³êdów CGI. cgi.tcl mo¿e byæ u¿ywane tak¿e do generowania statycznego
HTML-a. Pozwala to na umieszczanie w HTML-u elementów programów w
HTML-u, takich jak zmienne, if/then/else, operacje na plikach itp. Na
przyk³ad, HTML nie ma zmiennych, wiêc je¶li u¿ywa siê tego samego
odno¶nika wielokrotnie na stronie, i w pewnym momencie on siê zmienia,
trzeba uaktualniæ ka¿de u¿ycie tego odno¶nika, byæ mo¿e na setkach
stron. Dziêki zapisaniu odno¶nika w zmiennej Tcl, wystarczy zmieniæ
tylko to miejsce, gdzie zmienna jest zdefiniowana. Znacznie u³atwia to
utrzymywanie stron. Jest to tylko ma³y przyk³ad zalet cgi.tcl.

%prep
%setup  -q -n %{name}-%{_mainver}
%patch0 -p1

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	SCRIPTDIR=%{_packagedir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README doc/*.txt example
%{_packagedir}/*.tcl
%{_mandir}/man3/*
