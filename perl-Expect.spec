#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Expect
%define		pnam	Expect
Summary:	Expect - Expect for Perl
Summary(pl):	Expect - Expect dla Perla
Name:		perl-Expect
Version:	1.15
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	e717952b79c740121c18a1958b1bd6bb
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-IO-Tty
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Expect Perl module is a successor of Comm.pl and a descendent of
Chat.pl.  It more closely resembles the Tcl Expect language than its
predecessors.  It does not contain any of the networking code found in
Comm.pl.  I suspect this would be obsolete anyway given the advent of
IO::Socket and external tools such as netcat.

%description -l pl
Modu³ Perla Expect jest nastêpc± Comm.pl i potomkiem Chat.pl. Bardziej
przypomina on jêzyk Tcl Expect ni¿ jego poprzednicy. Nie zawiera kodu
sieciowego, który by³ obecny w Comm.pl. Prawdopodobnie powinien byæ
uznany za przestarza³y wraz z ukazaniem siê IO::Socket i zewnêtrznych
narzêdzi, takich jak netcat.

%prep
%setup -q -n %{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README tutorial
%{perl_vendorlib}/Expect.pm
%{_mandir}/man3/*
