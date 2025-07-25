#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	Expect
%define		pnam	Expect
Summary:	Expect - Expect for Perl
Summary(pl.UTF-8):	Expect - Expect dla Perla
Name:		perl-Expect
Version:	1.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Expect/%{pnam}-%{version}.tar.gz
# Source0-md5:	a151b0dc4d1a35c73941c65b7c26da5b
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Expect/
BuildRequires:	perl-IO-Tty >= 1.03
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Expect Perl module is a successor of Comm.pl and a descendent of
Chat.pl.  It more closely resembles the Tcl Expect language than its
predecessors.  It does not contain any of the networking code found in
Comm.pl.  I suspect this would be obsolete anyway given the advent of
IO::Socket and external tools such as netcat.

%description -l pl.UTF-8
Moduł Perla Expect jest następcą Comm.pl i potomkiem Chat.pl. Bardziej
przypomina on język Tcl Expect niż jego poprzednicy. Nie zawiera kodu
sieciowego, który był obecny w Comm.pl. Prawdopodobnie powinien być
uznany za przestarzały wraz z ukazaniem się IO::Socket i zewnętrznych
narzędzi, takich jak netcat.

%prep
%setup -q -n %{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Expect

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README tutorial
%{perl_vendorlib}/Expect.pm
%{perl_vendorlib}/Expect
%{_mandir}/man3/*
