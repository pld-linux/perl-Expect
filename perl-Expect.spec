%include	/usr/lib/rpm/macros.perl
Summary:	Expect perl module
Summary(pl):	Modu³ perla Expect
Name:		perl-Expect
Version:	1.15
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Expect/Expect-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	perl-IO-Tty
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expect Perl module - expect for Perl. In this version perl-IO-Stty
module is not required, but recommended (needed to change pty mode).

%description -l pl
Modu³ Perla Expect - expect dla Perla. W tej wersji modu³ perl-IO-Stty
nie jest ju¿ wymagany, ale zalecany (potrzebny do zmiany trybu
pseudoterminala).

%prep
%setup -q -n Expect-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README tutorial
%{perl_sitelib}/Expect.pm
%{_mandir}/man3/*
