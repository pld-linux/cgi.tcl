Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(pl):	Tool Command Language - jêzyk skryptowy z bibliotekami dynamicznymi
Name:		cgi.tcl
%define		_mainver	1.6
Version:	1.6.1
Release:	1
License:	Public Domain
Group:		Development/Languages/Tcl
Source0:	http://expect.nist.gov/%{name}/%{name}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://expect.nist.gov/cgi.tcl/
BuildRequires:	autoconf
Requires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_packagedir	%{_libdir}/tcl8.3/cgi%{_mainver}

%description
cgi.tcl is the CGI support library for Tcl programmers. The library is
very thorough - it supports forms, tables, cookies, file upload,
plug-ins, JavaScript, Netscape extensions, etc, etc. It also provides
very convenient support for debugging and handling CGI errors. cgi.tcl
can also be used for generating static html (such as this page). This
enables you to get programming features into HTML, such as variables,
if/then/else, file I/O, etc. For example, HTML lacks variables so if
you repeatedly use a link on a page and one day the link changes,
you've got to update every use of the link, possibly on hundreds of
pages. By storing the link in a Tcl variable, you can just change the
one place where the variable is defined. This makes maintenance much
easier. This is just a tiny example of the benefits cgi.tcl provides.

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
%attr(644,root,root) %{_packagedir}/*.tcl
%{_mandir}/man3/*
