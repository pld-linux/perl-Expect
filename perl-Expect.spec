%include	/usr/lib/rpm/macros.perl
%define		pdir	Expect
%define		pnam	Expect
Summary:	Expect Perl module
Summary(cs):	Modul Expect pro Perl
Summary(da):	Perlmodul Expect
Summary(de):	Expect Perl Modul
Summary(es):	Módulo de Perl Expect
Summary(fr):	Module Perl Expect
Summary(it):	Modulo di Perl Expect
Summary(ja):	Expect Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Expect ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Expect
Summary(pl):	Modu³ perla Expect
Summary(pt_BR):	Módulo Perl Expect
Summary(pt):	Módulo de Perl Expect
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Expect
Summary(sv):	Expect Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Expect
Summary(zh_CN):	Expect Perl Ä£¿é
Name:		perl-Expect
Version:	1.15
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	perl-IO-Tty
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%setup -q -n %{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL
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
